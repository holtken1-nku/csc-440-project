# Steps to "compile"

1. Setup a web server to serve the json files in the DATA folder.

2. Install [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

3. Go to the Grafana web interface

4. Click Connections > Add new connection

5. Search for "Infinity", click on it, then Install (top right)

6. "Add new data source" 

7. In the "Name" field enter: pl_standings

8. Go to the "URL, Headers & Params" tab

9. Enter http://<address to web server>/pl_standings.json

10. Click New > Import

11. Import the json file in the Source_Code/frontend-grafana folder.

12. The graph will (hopefully) show up with all the data in it


