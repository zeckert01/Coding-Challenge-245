# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:58:28 2019

@author: zecke
"""
import math
import re
from collections import Counter
import huffman

def main():
    print("Sample Decoder Output 1: \n%s" % decodeFile("SampleDecoderInput1.txt"))
    print("Sample Decoder Output 2: \n%s" % decodeFile("SampleDecoderInput2.txt"))
    print("Challenge Decoder Output: \n%s" % decodeFile("ChallengeDecoderInput.txt"))

    with open("SampleEncoderOutput1.txt","w") as f:
        f.write(encodeFile("SampleEncoderInput1.txt"))
    print("Testing Encoder Sample Input 1: \n%s" % decodeFile("SampleEncoderOutput1.txt"))

    with open("SampleEncoderOutput2.txt","w") as f:
        f.write(encodeFile("SampleEncoderInput2.txt"))
    print("Testing Encoder Sample Input 2: \n%s" % decodeFile("SampleEncoderOutput2.txt"))

    with open("ChallengeEncoderOutput.txt","w") as f:
        f.write(encodeFile("ChallengeEncoderInput.txt"))
    print("Testing Encoder Challenge Input: \n%s" % decodeFile("ChallengeEncoderOutput.txt"))



def encodeFile(fileName):
    try:
        file = open(fileName,"r")
    except:
        print("Invalid filename")
        return ""
    fileContents = file.read().rstrip()
    freq = Counter(re.sub("[^A-Za-z]","",fileContents)).items()
    codec = huffman.codebook(freq)

    output = ""
    for key in codec:
        codec[key] = codec[key].replace('0','g').replace('1','G')
        output += "%s " % key
        output += "%s " % codec[key]

    output += "\n"

    for ch in list(fileContents):
        try:
            output += codec[ch]
        except:
            output += ch
    return(output)


def decodeFile(fileName):
    try:
        file = open(fileName,"r")
    except:
        print("Invalid filename")
        return ""
    fileContents = file.readlines()
    file.close()

    keyStrings = fileContents[0].split()
    code = {}
    for i in range(math.ceil((len(keyStrings)-1)/2)):
        code[keyStrings[2*i + 1]] = keyStrings[2*i]

    output = ""
    key = ""
    for line in fileContents[1:]:
        for ch in list(line):
            try:
                if not (ch == "g" or ch == "G"):
                    output += ch
                    key = ""
                else:
                    key += ch
                    output += code[key]
                    key = ""
            except:
                continue
    return output

if __name__ == "__main__":
    main()