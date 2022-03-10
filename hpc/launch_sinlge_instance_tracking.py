import os
import tempfile
import time
import argparse

parser = argparse.ArgumentParser(description="Description of your program")

parser.add_argument(
"-m", "--model_path", help="video path", required=True
) 

parser.add_argument(
"-t", "--model_type", help="video path", required=True
)

parser.add_argument(
"-p", "--partition", help="video path", required=True
)

parser.add_argument(
"-a", "--account", help="video path", required=True
)

args = vars(parser.parse_args())

videos = [x for x in os.listdir('hpc/videos_to_track') if x[-4:] == ".avi"]

for video in videos:
    output = video.split('.')[0]+'_tracking'
    
    SBATCH_STRING = """#!/bin/sh
    
#SBATCH --account={account}
#SBATCH --partition={partition}
#SBATCH --job-name={jobname}
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --time=48:00:00
#SBATCH --mem=40GB

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/kaulg/miniconda3/lib/

export PATH=/home/kaulg/miniconda3/envs/deepAnimalToolkit/bin:$PATH

cd /scratch/justincj_root/justincj/kaulg/deep-animal-toolkit 

python tracking/single_instance.py -v hpc/videos_to_track/{video} -o hpc/output/{output} -t {model_type} -m {model}

"""
    

    SBATCH_STRING = SBATCH_STRING.format(
        video = video,
        jobname = 'deepAnimalToolkit',
        output = output,
        model = args["model_path"],        
        model_type = args["model_type"],
        partition = args["partition"],
        account = args["account"]
    )
    
    dirpath = tempfile.mkdtemp()
    # print(SBATCH_STRING)
    with open(os.path.join(dirpath, "scr.sh"), "w") as tmpfile:
        tmpfile.write(SBATCH_STRING)
    os.system(f"sbatch {os.path.join(dirpath, 'scr.sh')}")
    print(f"Launched from {os.path.join(dirpath, 'scr.sh')}")
    time.sleep(1)
