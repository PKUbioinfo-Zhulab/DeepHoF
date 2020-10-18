import pandas as pd
import numpy as np
import sys
# import commands
from tqdm import tqdm
import os


def list_files(path, suffix):
    dirs = os.listdir(path)
    csv_files = []
    for i in dirs:
        if os.path.splitext(i)[1] == suffix:
            csv_files.append(i)
    return csv_files


if __name__ == "__main__":
    fasta_files = list_files('./tmp', '.fasta')
    print(fasta_files)
    # """
    if len(fasta_files) == 2:
        os.system('grep ">" ./tmp/100_400bp.fasta >./tmp/head1.txt')
        os.system("sed -i 's/.//' ./tmp/head1.txt")
        head = pd.read_csv('./tmp/head1.txt', sep='%%', header=None)
        head.to_csv('./tmp/head1.txt', sep='\t', header=None, index=False)
        os.system("paste -d '\t' ./tmp/head1.txt ./tmp/group1_predicts.txt >./tmp/group1_predicts.csv")
        os.system('grep ">" ./tmp/400_800bp.fasta >./tmp/head2.txt')
        os.system("sed -i 's/.//' ./tmp/head2.txt")
        head = pd.read_csv('./tmp/head2.txt', sep='%%', header=None)
        head.to_csv('./tmp/head2.txt', sep='\t', header=None, index=False)
        os.system("paste -d '\t' ./tmp/head2.txt ./tmp/group2_predicts.txt >./tmp/group2_predicts.csv")
    else:
        if "100_400bp.fasta" in fasta_files:
            os.system('grep ">" ./tmp/100_400bp.fasta >./tmp/head1.txt')
            os.system("sed -i 's/.//' ./tmp/head1.txt")
            head = pd.read_csv('./tmp/head1.txt', sep='%%', header=None)
            print(head)
            head.to_csv('./tmp/head1.txt', sep='\t', header=None, index=False)
            # os.system("sed -i '1d' ./tmp/group1_predicts.txt")
            os.system("paste -d '\t' ./tmp/head1.txt ./tmp/group1_predicts.txt  >./tmp/group1_predicts.csv")
        if "400_800bp.fasta" in fasta_files:
            os.system('grep ">" ./tmp/400_800bp.fasta >./tmp/head2.txt')
            os.system("sed -i 's/.//' ./tmp/head2.txt")
            head = pd.read_csv('./tmp/head2.txt', sep='%%', header=None)
            head.to_csv('./tmp/head2.txt', sep='\t', header=None, index=False)
            os.system("paste -d '\t' ./tmp/head2.txt ./tmp/group2_predicts.txt >./tmp/group2_predicts.csv")

    csv_files = list_files('./tmp', '.csv')
    df = pd.DataFrame(
        columns=["virus", "length", "full_length", "plant score", "germ score", "invertebrate score", "vertebrate score", "human score"])
    for i in range(len(csv_files)):
        tmp = pd.read_csv('./tmp/' + csv_files[i], header=None, sep='\t')
        tmp.columns = ["virus", "length", "full_length", "plant score", "germ score", "invertebrate score", "vertebrate score", "human score"]
        if i == 0:
            df = tmp
        else:
            df = pd.concat([df, tmp])
    df['prob'] = df['length'] / df['full_length']
    df['plant score'] = df['prob'] * df['plant score']
    df['germ score'] = df['prob'] * df['germ score']
    df['invertebrate score'] = df['prob'] * df['invertebrate score']
    df['vertebrate score'] = df['prob'] * df['vertebrate score']
    df['human score'] = df['prob'] * df['human score']
    df = df.drop('length', 1)
    df = df.drop('full_length', 1)
    df = df.drop('prob', 1)
    df = df.groupby('virus').agg(np.sum)
    df.to_csv('./tmp/score.txt', sep='\t', index=True)