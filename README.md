# Module7: QR CodeMaker

## My Github Repository
![Github Repo](/samples/QRCode_20261021004919.png "My QR Code Link")

## My DockerHub Image
![Docker QR Image](/samples/QRCode_20261021005415.png "My QR Image Link")

## Local Usage:
Build the image
```
docker compose build qr_code_app
```
Generate QR code link to specified URL
```
 docker compose run qr_code_app --url <specified URL>
```
### Examples:
Generate QR code link to this Github repo
```
docker compose run qr_code_app --url https://github.com/obi-a/assignment7-qr-codemaker
```

Generate QR code link to the docker image
```
docker compose run qr_code_app --url https://hub.docker.com/r/decodeinvesting/qr_codemaker
```

### Testing
To run tests
```
docker compose run --rm --build --entrypoint python qr_code_app -m pytest -v
```
