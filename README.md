# Script for show system metrics

Python script which allow you show cpu and memory metrics

## Requirements
 
* python 2 or 3 version
* psutil (Cross-platform lib for process and system monitoring in Python) 

## Usage

python system_metrics.py `param`
### Param: 
 
Param name | Description
------------ | -------------
cpu | prints CPU metrics
mem | prints RAM metrics

## Example output

### python system_metrics.py cpu

```system.cpu.idle 76083.57
system.cpu.user 61.98
system.cpu.guest 0.0
system.cpu.iowait 190.72
system.cpu.stolen 0.0
system.cpu.system 63.3 
```


### python system_metrics.py mem

```virtual total 2076434432
virtual used 696209408
virtual free 127070208
virtual shared 1130496
swap total 1073737728
swap used 593920
swap free 1073143808
```

## Usage Docker

Docker image with all dependencies. Just run docker with one of both params, like:

`docker run -t --rm yevheniilukashenko/metrics:latest cpu`

or

`docker run -t --rm yevheniilukashenko/metrics:latest mem`

Docker image avalible in [docker hub](https://hub.docker.com/r/yevheniilukashenko/metrics/)
