import hyperline

# Create spark session
spark = hyperline.get_spark_session(app_name="lucidity-support")

# Load data from BigQuery
aave_pool_event_data = spark.read.format('bigquery') \
  .option('table',  'blockchain-etl.ethereum_aave.Pool_v3_event_ReserveDataUpdated') \
  .load()

aave_pool_event_withdraw_data = spark.read.format('bigquery') \
  .option('table',  'blockchain-etl.ethereum_aave.Pool_v3_event_Withdraw') \
  .load()

tokens.erc20 

aave_pool_event_data.createOrReplaceTempView('ethereum_aave_Pool_v3_event_ReserveDataUpdated')
aave_pool_event_withdraw_data.createOrReplaceTempView('ethereum_aave_Pool_v3_event_Withdraw')

query = """WITH
  current_market_ AS (
    SELECT
      r.*,
      t.symbol,
      RANK() OVER (
        PARTITION BY
          t.symbol
        ORDER BY
          r.block_number DESC,
          r.log_index DESC
      ) AS rank 
    FROM
      ethereum_aave_Pool_v3_event_ReserveDataUpdated AS r
      INNER JOIN (
        SELECT
          reserve,
          MAX(block_number) AS max_block
        FROM
          ethereum_aave_Pool_v3_event_ReserveDataUpdated
        GROUP BY
          reserve
      ) AS last_updated ON last_updated.max_block = r.block_number
      AND last_updated.reserve = r.reserve
      LEFT JOIN tokens.erc20 AS t ON t.contract_address = r.reserve
      AND t.blockchain = 'ethereum'
  ),
  current_market AS (
    SELECT
      * 
    FROM 
      current_market_
    WHERE
      rank = 1
  ),
  supplies_ AS (
    SELECT
      s.evt_tx_hash,
      CONCAT(cast(s.evt_block_number as varchar(64)), '-', cast(s.evt_index as varchar(64))) AS borrow_id,
      s.evt_block_time,
      s.evt_block_number,
      t.symbol,
      t.decimals,
      amount,
      s.onBehalfOf,
      s.reserve,
      u.liquidityIndex,
      RANK() OVER (
        PARTITION BY
          s.evt_block_number,
          s.evt_index
        ORDER BY
          u.evt_index DESC
      ) AS rnk
    FROM
      aave_v3_ethereum.Pool_evt_Supply AS s
      LEFT JOIN tokens.erc20 AS t ON t.contract_address = s.reserve
      AND t.blockchain = 'ethereum'
      LEFT JOIN ethereum_aave_Pool_v3_event_ReserveDataUpdated AS u ON s.evt_block_number = u.evt_block_number
      AND u.evt_index < s.evt_index
      AND u.evt_tx_hash = s.evt_tx_hash
      AND u.reserve = s.reserve
  ),
  supplies_scaled AS (
    SELECT
      current_market.symbol,
      SUM(
        amount / POWER(10, s.decimals) / s.liquidityIndex * POWER(10, 27)
      ) AS supplied_total_scaledAtokens
    FROM
      supplies_ AS s
      LEFT JOIN current_market ON current_market.reserve = s.reserve
      AND current_market.rank = 1
    WHERE
      rnk = 1
    GROUP BY
      current_market.symbol
  ),
  withdraws_ AS (
    SELECT
      s.evt_tx_hash,
      CONCAT(cast(s.evt_block_number as varchar(64)), '-', cast(s.evt_index as varchar(64))) AS borrow_id,
      s.evt_block_time,
      s.evt_block_number,
      t.symbol,
      t.decimals,
      amount,
      s.reserve,
      u.liquidityIndex,
      RANK() OVER (
        PARTITION BY
          s.evt_block_number,
          s.evt_index
        ORDER BY
          u.evt_index DESC
      ) AS rnk
    FROM
      ethereum_aave_Pool_v3_event_Withdraw AS s
      LEFT JOIN tokens.erc20 AS t ON t.contract_address = s.reserve
      AND t.blockchain = 'ethereum'
      LEFT JOIN ethereum_aave_Pool_v3_event_ReserveDataUpdated AS u ON s.block_number = u.block_number
      AND u.evt_index < s.evt_index
      AND u.evt_tx_hash = s.evt_tx_hash
      AND u.reserve = s.reserve
  ),
  withdraws_scaled AS (
    SELECT
      current_market.symbol,
      SUM(
        amount / POWER(10, a.decimals) / a.liquidityIndex * POWER(10, 27)
      ) AS withdrawn_total_scaledAtokens
    FROM
      withdraws_ AS a
      LEFT JOIN current_market ON current_market.reserve = a.reserve
      AND current_market.rank = 1
    WHERE
      rnk = 1
    GROUP BY
      current_market.symbol
  ),
  liquidations_ AS (
    SELECT
      s.evt_tx_hash,
      CONCAT(cast(s.evt_block_number as varchar(64)), '-', cast(s.evt_index as varchar(64))) AS borrow_id,
      s.evt_block_time,
      s.evt_block_number,
      t.symbol,
      t.decimals,
      CAST(liquidatedCollateralAmount AS DOUBLE) AS amount,
      s.collateralAsset AS reserve,
      u.liquidityIndex,
      RANK() OVER (
        PARTITION BY
          s.evt_block_number,
          s.evt_index
        ORDER BY
          u.evt_index DESC
      ) AS rnk
    FROM
      aave_v3_ethereum.Pool_evt_LiquidationCall AS s
      LEFT JOIN tokens.erc20 AS t ON t.contract_address = s.collateralAsset
      AND t.blockchain = 'ethereum'
      LEFT JOIN ethereum_aave_Pool_v3_event_ReserveDataUpdated AS u ON s.evt_block_number = u.evt_block_number
      AND u.evt_index < s.evt_index
      AND u.evt_tx_hash = s.evt_tx_hash
      AND u.reserve = s.collateralAsset
  ),
  liquidations_scaled AS (
    SELECT
      current_market.symbol,
      SUM(
        amount / POWER(10, a.decimals) / a.liquidityIndex * POWER(10, 27)
      ) AS liquidated_total_scaledAtokens
    FROM
      liquidations_ AS a
      LEFT JOIN current_market ON current_market.reserve = a.reserve
      AND current_market.rank = 1
    WHERE
      rnk = 1
    GROUP BY
      current_market.symbol
  ),
  repaywithatokens_ AS (
    SELECT
      r.evt_tx_hash,
      CONCAT(cast(r.evt_block_number as varchar(64)), '-', cast(r.evt_index as varchar(64))) AS borrow_id,
      r.evt_block_time,
      r.evt_block_number,
      t.symbol,
      t.decimals,
      amount,
      r.reserve,
      u.liquidityIndex,
      RANK() OVER (
        PARTITION BY
          r.evt_block_number,
          r.evt_index
        ORDER BY
          u.evt_index DESC
      ) AS rnk
    FROM
      aave_v3_ethereum.Pool_evt_Repay AS r
      INNER JOIN tokens.erc20 AS t ON t.contract_address = r.reserve
      AND t.blockchain = 'ethereum'
      LEFT JOIN ethereum_aave_Pool_v3_event_ReserveDataUpdated AS u ON u.evt_block_number = r.evt_block_number
      AND u.evt_index < r.evt_index
      AND u.evt_tx_hash = r.evt_tx_hash
      AND u.reserve = r.reserve
    WHERE
      r.useATokens = TRUE
  ),
  repays_scaled AS (
    SELECT
      current_market.symbol,
      SUM(
        amount / POWER(10, a.decimals) / a.liquidityIndex * POWER(10, 27)
      ) AS repaidwithcollateral_total_scaledAtokens
    FROM
      repaywithatokens_ AS a
      LEFT JOIN current_market ON current_market.reserve = a.reserve
      AND current_market.rank = 1
    WHERE
      rnk = 1
    GROUP BY
      current_market.symbol
  ),
  scaled_atokens_remaining AS (
    SELECT
      supplies_scaled.symbol,
      supplied_total_scaledAtokens,
      liquidated_total_scaledAtokens,
      withdrawn_total_scaledAtokens,
      COALESCE(
        repays_scaled.repaidwithcollateral_total_scaledAtokens,
        0
      ) AS repaidwithcollateral_total_scaledAtokens,
      (
        supplied_total_scaledAtokens - COALESCE(liquidated_total_scaledAtokens, 0) - COALESCE(withdrawn_total_scaledAtokens, 0) - COALESCE(
          repays_scaled.repaidwithcollateral_total_scaledAtokens,
          0
        )
      ) AS scaled_atokens_supplied,
      (
        supplied_total_scaledAtokens - COALESCE(liquidated_total_scaledAtokens, 0) - COALESCE(withdrawn_total_scaledAtokens, 0) - COALESCE(
          repays_scaled.repaidwithcollateral_total_scaledAtokens,
          0
        )
      ) * current_market.liquidityIndex / POWER(10, 27) AS current_aTokens,
      p.price AS current_price,
      p.minute AS last_price_update,
      p.price * (
        supplied_total_scaledAtokens - COALESCE(liquidated_total_scaledAtokens, 0) - COALESCE(withdrawn_total_scaledAtokens, 0) - COALESCE(
          repays_scaled.repaidwithcollateral_total_scaledAtokens,
          0
        )
      ) * current_market.liquidityIndex / POWER(10, 27) AS value_deposited,
      p.price * (
        supplied_total_scaledAtokens - COALESCE(liquidated_total_scaledAtokens, 0) - COALESCE(withdrawn_total_scaledAtokens, 0) - COALESCE(
          repays_scaled.repaidwithcollateral_total_scaledAtokens,
          0
        )
      ) * current_market.liquidityIndex / POWER(10, 27) / 1000000 AS value_deposited_m
    FROM
      supplies_scaled
      LEFT JOIN liquidations_scaled ON liquidations_scaled.symbol = supplies_scaled.symbol
      LEFT JOIN withdraws_scaled ON withdraws_scaled.symbol = supplies_scaled.symbol
      LEFT JOIN current_market ON current_market.symbol = supplies_scaled.symbol
      LEFT JOIN repays_scaled ON repays_scaled.symbol = supplies_scaled.symbol
      LEFT JOIN prices.usd_latest AS p ON p.blockchain = 'ethereum'
      AND p.contract_address = current_market.reserve
  )
SELECT
  SUM(CAST(value_deposited AS DOUBLE)) / 1000000000 AS current_market_size
FROM
  scaled_atokens_remaining
"""

ICEBERG_DB_NAME = "ws_async_datalake.support"
spark.sql("CREATE DATABASE IF NOT EXISTS " + ICEBERG_DB_NAME)
results = spark.sql(query)

table_name = ICEBERG_DB_NAME + ".lucidity_support"
results.write \
  .format("iceberg") \
  .mode("overwrite") \
  .saveAsTable(table_name)


read_data = spark.read.table(table_name)   
read_data.show(truncate=False)
