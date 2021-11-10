# Truck optimizer

## Running

Edit the routes.txt and drivers.txt files, then run the following:

```bash
pip install --user -r requirements.txt
python run.py
```

to specify the files:
```bash
python --drivers drivers.txt --routes routes.txt 
```


Or with docker:
```bash
docker run --rm -it $(docker build -q .)
```


## generate data

If you need to generate data for testing purposes, run:
```bash
python generate.py
```