from backend.blockchain.blockchain import Blockchain
import time
from backend.config import SECONDS

blockchain=Blockchain()

times =[]

for i in range(1000):
    start_t=time.time_ns()
    blockchain.addblock(i)
    end_t=time.time_ns()

    time_to_mine= (end_t-start_t)/SECONDS
    times.append(time_to_mine)

    avg_t=sum(times)/len(times)
    print(f'New block difficulty :{blockchain.chain[-1].difficulty}')
    print(f'Time to mine new Block :{time_to_mine}s')
    print(f'Avegrage time to add block :{avg_t}s\n')
