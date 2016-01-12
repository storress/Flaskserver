# Flaskserver

How to use:

Send a 'POST' request to the url localhost:5000/echo
with a json body with this format :

        {'file' : <file> ,
         'network_info' : <network_info>,
         'speed_test' : <speed_test>}

The server returns the same json

Example POST localhost:5000/echo :

            {"file": "http://michotastico.github.io/assets/images/space.jpg",
            "network_info": {
                "googleInformation": [
                    "Club Hípico 816-888",
                    " Santiago",
                    " Santiago",
                    " Región Metropolitana",
                    " Chile"
                ],
                "ipApiInformation": {
                    "as": "AS6429 Telmex Chile Internet S.A.",
                    "city": "Santiago de Chile",
                    "country": "Chile",
                    "countryCode": "CL",
                    "isp": "Telmex Chile Internet S.A.",
                    "lat": -33.45,
                    "lon": -70.6667,
                    "mobile": false,
                    "org": "Universidad de Chile",
                    "proxy": false,
                    "query": "200.27.xx.xxx",
                    "region": "RM",
                    "regionName": "Metropolitana",
                    "reverse": "",
                    "status": "success",
                    "timezone": "America/Santiago"
                },
                "currentOs": "Linux",
                "networkType": "Unknown",
                "coordinates": [
                    -33.458012200000006,
                    -70.6645187
                ]
            },
            "speed_test": {
                "downloadSpeed": 14.236759709504263,
                "testTime": 12.668,
                "testResult": {
                    "start": 1452626695541,
                    "firstByte": 1452626696429,
                    "url": "http://michotastico.github.io/assets/images/space.jpg?cacheBuster=1452626695541",
                    "dataSizeKB": 22543.909,
                    "end": 1452626708209,
                    "latency": 888,
                    "throughput": 1913.74,
                    "throughPutSpeedClass": {
                        "name": "3G_HSPA",
                        "latency": 200,
                        "throughput": 1000
                    },
                    "latencySpeedClass": {
                        "name": "DAIL_UP",
                        "latency": 2000,
                        "throughput": 2.4
                    }
                },
                "file": "http://michotastico.github.io/assets/images/space.jpg"
            }
        }

returns:

          {
            "file": "http://michotastico.github.io/assets/images/space.jpg",
            "network_info": {
              "coordinates": [
                -33.458012200000006,
                -70.6645187
              ],
              "currentOs": "Linux",
              "googleInformation": [
                "Club Hípico 816-888",
                " Santiago",
                " Santiago",
                " Región Metropolitana",
                " Chile"
              ],
              "ipApiInformation": {
                "as": "AS6429 Telmex Chile Internet S.A.",
                "city": "Santiago de Chile",
                "country": "Chile",
                "countryCode": "CL",
                "isp": "Telmex Chile Internet S.A.",
                "lat": -33.45,
                "lon": -70.6667,
                "mobile": false,
                "org": "Universidad de Chile",
                "proxy": false,
                "query": "200.27.xx.xxx",
                "region": "RM",
                "regionName": "Metropolitana",
                "reverse": "",
                "status": "success",
                "timezone": "America/Santiago"
              },
              "networkType": "Unknown"
            },
            "speed_test": {
              "downloadSpeed": 14.236759709504263,
              "file": "http://michotastico.github.io/assets/images/space.jpg",
              "testResult": {
                "dataSizeKB": 22543.909,
                "end": 1452626708209,
                "firstByte": 1452626696429,
                "latency": 888,
                "latencySpeedClass": {
                  "latency": 2000,
                  "name": "DAIL_UP",
                  "throughput": 2.4
                },
                "start": 1452626695541,
                "throughPutSpeedClass": {
                  "latency": 200,
                  "name": "3G_HSPA",
                  "throughput": 1000
                },
                "throughput": 1913.74,
                "url": "http://michotastico.github.io/assets/images/space.jpg?cacheBuster=1452626695541"
              },
              "testTime": 12.668
            }
          }