Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"
  
  
  config.vm.define "webserver" do |webserver|
  webserver.vm.box = "bento/ubuntu-22.04"
  webserver.vm.network "private_network", type: "static", ip: "192.168.1.30"
  webserver.vm.hostname = "webserver"
  webserver.vm.provision "shell", inline: <<-SHELL
  
    sudo apt-get update

    wget https://github.com/prometheus/prometheus/releases/download/v2.37.6/prometheus-2.37.6.linux-amd64.tar.gz
    tar xvf prometheus-2.37.6.linux-amd64.tar.gz
    sudo cp prometheus-2.37.6.linux-amd64/prometheus /usr/local/bin/
    sudo cp prometheus-2.37.6.linux-amd64/promtool /usr/local/bin/
    sudo mkdir /etc/prometheus /var/lib/prometheus
    sudo cp prometheus-2.37.6.linux-amd64/prometheus.yml /etc/prometheus/prometheus.yml
    rm -rf prometheus-2.37.6.linux-amd64.tar.gz prometheus-2.37.6.linux-amd64

    wget https://github.com/prometheus/alertmanager/releases/download/v0.26.0/alertmanager-0.26.0.linux-amd64.tar.gz
    tar xvf alertmanager-0.26.0.linux-amd64.tar.gz
    sudo cp alertmanager-0.26.0.linux-amd64/alertmanager /usr/local/bin/
    sudo mkdir /etc/alertmanager/
    sudo cp alertmanager-0.26.0.linux-amd64/amtool /etc/alertmanager
    rm -rf alertmanager-0.26.0.linux-amd64.tar.gz alertmanager-0.26.0.linux-amd64

    sudo apt-get install -y software-properties-common
    sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
    sudo wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install -y grafana

  SHELL
  end
  
  config.vm.define "mysql" do |mysql|
  mysql.vm.box = "bento/ubuntu-22.04"
  mysql.vm.network "private_network", type: "static", ip: "192.168.1.20"
  mysql.vm.hostname = "mysql"
  mysql.vm.provision "shell", inline: <<-SHELL
  
       
    sudo apt-get update
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password vagrant'
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password vagrant'
    sudo apt-get install -y mysql-server
    
    wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
    tar xvf node_exporter-1.5.0.linux-amd64.tar.gz
    sudo cp node_exporter-1.5.0.linux-amd64/node_exporter /usr/local/bin/
    rm -rf node_exporter-1.5.0.linux-amd64.tar.gz node_exporter-1.5.0.linux-amd64

    wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.14.0/mysqld_exporter-0.14.0.linux-amd64.tar.gz
    tar xvf mysqld_exporter-0.14.0.linux-amd64.tar.gz
    sudo cp mysqld_exporter-0.14.0.linux-amd64/mysqld_exporter /usr/local/bin/
    sudo mkdir /etc/mysqld_exporter/
    rm -rf mysqld_exporter-0.14.0.linux-amd64.tar.gz mysqld_exporter-0.14.0.linux-amd64
    
    sudo apt-get install mysql-client
    
    echo "CREATE DATABASE Shop;" | mysql -u root -pvagrant  
    
  SHELL
  end
end
