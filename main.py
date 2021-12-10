from google.cloud import bigquery
from pgsql import query
import sql


def get_bigquery_data():
    client = bigquery.Client()
    big_query = client.query(
        """
        WITH cte AS(
            SELECT geo_id, sub_region_1, sub_region_2, retail_and_recreation_percent_change_from_baseline 
                FROM `bigquery-public-data.census_bureau_acs.county_2017_1yr`
                JOIN `bigquery-public-data.covid19_google_mobility.mobility_report` on geo_id || '.0' = census_fips_code
                WHERE median_rent < 2000 AND median_age < 30
                --AND retail_and_recreation_percent_change_from_baseline> -15 
        )
        
        SELECT geo_id, sub_region_1, sub_region_2, avg(retail_and_recreation_percent_change_from_baseline) AS sales_vector
        FROM cte 
        GROUP BY geo_id, sub_region_1, sub_region_2
        HAVING sales_vector > -15
        order by sales_vector;
        """
    )
    for row in big_query.result():
        # print(row)
        query(sql.insert_viable_countys, row)


if __name__ == '__main__':
    query(sql.create_schema, 'create schema')
    query(sql.create_table, 'create table')
    query(sql.truncate_table, 'truncate table')

    get_bigquery_data()
