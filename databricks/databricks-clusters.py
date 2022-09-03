import os
import pathlib
from pprint import pprint

from databricks_cli.clusters.api import ClusterApi
from databricks_cli.sdk.api_client import ApiClient
from obfuscate_op import o2

#os.environ["DATABRICKS_HOST"] = "https://xyz.azuredatabricks.net"
#os.environ["DATABRICKS_TOKEN"] = "dapi..."

api_client = ApiClient(
  host = os.getenv('DATABRICKS_HOST'),
  token = os.getenv('DATABRICKS_TOKEN')
)

clusters_api = ClusterApi(api_client)
clusters_list = clusters_api.list_clusters()

print("Cluster name, cluster ID")
for cluster in clusters_list['clusters']:
  pprint(o2(clusters_api.get_cluster_by_name(cluster['cluster_name'])))

# cluster = clusters_api.get_cluster_by_name('DS 9.1 ML HC - Small')
#pprint(cluster['autoscale'])
#pprint(cluster)


