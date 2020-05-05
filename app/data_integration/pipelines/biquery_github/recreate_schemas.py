from app.data_integration.pipelines.biquery_github import bigquery

bigquery.remove_bigquery_dataset('bq_dwh', 'gh_tmp')
bigquery.create_bigquery_dataset('bq_dwh', 'gh_tmp')

bigquery.remove_bigquery_dataset('bq_dwh', 'gh_dim_next')
bigquery.create_bigquery_dataset('bq_dwh', 'gh_dim_next')
