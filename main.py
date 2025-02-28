'''
You can run all three bots in one terminal instance by executing this file.

You can also run every bot separately for easier testing and logic visualization
'''

import multiprocessing
import trade_tailer as trader
import risk_manager
import trade_monitor
import os

user_address = os.getenv('PROXY_WALLET')

def run_trade_monitor():
    trade_monitor.main()

def run_trader():
    trader.run_trade_tailer()

def run_risk_manager():
    risk_manager.run_risk_manager(user_address)

if __name__ == "__main__":
    # Create separate processes for each function
    processes = [
        multiprocessing.Process(target=run_trade_monitor),
        multiprocessing.Process(target=run_trader),
        multiprocessing.Process(target=run_risk_manager)
    ]

    # Start each process
    for process in processes:
        process.start()