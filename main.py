from pathlib import Path
import csv

import cash_on_hand
import overheads
import ProfitandLoss

def main():
    overheads.overhead_function()
    cash_on_hand.coh_function()
    ProfitandLoss.profit_loss_function()

main()
file_path_write = Path.cwd()/'summaryreport.txt'
file_path_write.touch()

with file_path_write.open(mode='w', encoding="'UTF-8") as file:
    file.write("abc")