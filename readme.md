Use `Rsync` to sync the data

```
rsync -avz --progress 119:~/G/gpu-stat/172.18.240.119_gpu_log.csv ~/G/gpu-stat/
rsync -avz --progress 107:~/G/gpu-stat/172.18.240.107_gpu_log.csv ~/G/gpu-stat/
rsync -avz --progress 195:~/G/gpu-stat/172.18.240.195_gpu_log.csv ~/G/gpu-stat/
rsync -avz --progress 100:~/G/gpu-stat/172.18.240.100_gpu_log.csv ~/G/gpu-stat/
rsync -avz --progress 231:~/G/gpu-stat/172.18.240.231_gpu_log.csv ~/G/gpu-stat/
rsync -avz --progress 253:~/G/gpu-stat/172.17.240.253_gpu_log.csv ~/G/gpu-stat/
```
Run this in a crontab job by `crontab -e`

```
*/1 * * * * rsync -avz --progress 119:~/G/gpu-stat/172.18.240.119_gpu_log.csv ~/G/gpu-stat/
*/1 * * * * rsync -avz --progress 107:~/G/gpu-stat/172.18.240.107_gpu_log.csv ~/G/gpu-stat/
*/1 * * * * rsync -avz --progress 195:~/G/gpu-stat/172.18.240.195_gpu_log.csv ~/G/gpu-stat/
*/1 * * * * rsync -avz --progress 100:~/G/gpu-stat/172.18.240.100_gpu_log.csv ~/G/gpu-stat/
*/1 * * * * rsync -avz --progress 231:~/G/gpu-stat/172.18.240.231_gpu_log.csv ~/G/gpu-stat/
*/1 * * * * rsync -avz --progress 253:~/G/gpu-stat/172.17.240.253_gpu_log.csv ~/G/gpu-stat/
```


Run `streamlit run main.py --server.port 8080`
