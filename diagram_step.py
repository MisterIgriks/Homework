from diagrams import Diagram, Cluster
from diagrams.onprem.database import Mysql
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.monitoring import AlertManager, NodeExporter, MysqlExporter
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.aws.business import Workmail

with Diagram("Monitoring Architecture", show=False):

    with Cluster("VM1"):
        mysql_server = Mysql("MySQL Server")
        mysql_exporter = MysqlExporter("MySQL Exporter")
        node_exporter = NodeExporter("Node Exporter")

        mysql_server << mysql_exporter

    with Cluster("VM2"):
        prometheus = Prometheus("Prometheus")
        grafana = Grafana("Grafana")
        alert_manager = AlertManager("Alert Manager")

        prometheus >> alert_manager
        prometheus << grafana

    prometheus >> node_exporter
    prometheus >> mysql_exporter
	
    internet_grafana = Internet("Grafana Web Interface")
    internet_prometheus = Internet("Prometheus Web Interface")

    mail = Workmail("send to e-mail")
    alert_manager >> mail 

    internet_prometheus << prometheus
    internet_grafana << grafana
    
