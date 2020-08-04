curl -iX POST \
  'http://localhost:4041/iot/services' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
 "services": [
   {
     "apikey":      "4jggokgpepnvsb2uv4s40d59ov",
     "cbroker":     "http://orion:1026",
     "entity_type": "Thing",
     "resource":    ""
   }
 ]
}'

curl -iX POST \
  'http://localhost:4041/iot/devices' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
 "devices": [
   {
     "device_id":   "raspberry",
     "entity_name": "urn:ngsi-ld:Motion:001",
     "entity_type": "Motion",
     "protocol":    "PDI-IoTA-UltraLight",
     "transport":   "MQTT",
     "timezone":    "America/Brazil",
     "attributes": [
       { "object_id": "i", "name": "id_rasp", "type": "Integer" }, { "object_id": "t", "name": "time", "type": "String" }
     ]
   }
 ]
}
'

curl -iX POST \
  'http://localhost:4041/iot/devices' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
 "devices": [
   {
     "device_id":   "raspberry_controle",
     "entity_name": "urn:ngsi-ld:Motion:002",
     "entity_type": "Motion",
     "protocol":    "PDI-IoTA-UltraLight",
     "transport":   "MQTT",
     "timezone":    "America/Brazil",
     "attributes": [
       { "object_id": "i", "name": "id_rasp", "type": "Integer" }, { "object_id": "t", "name": "time", "type": "String" }
     ]
   }
 ]
}
'

curl -iX POST \
  'http://localhost:4041/iot/devices' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
 "devices": [
   {
     "device_id":   "relogio01",
     "entity_name": "urn:ngsi-ld:Motion:004",
     "entity_type": "Motion",
     "protocol":    "PDI-IoTA-UltraLight",
     "transport":   "MQTT",
     "timezone":    "America/Brazil",
     "attributes": [
       { "object_id": "i", "name": "inicio", "type": "String" }, { "object_id": "f", "name": "fim", "type": "String" }, { "object_id": "t", "name": "termino", "type": "Boolean" }
     ]
   }
 ]
}
'
