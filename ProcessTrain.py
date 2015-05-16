__author__ = 'ShadowWalker'
import sys

# 训练数据文件为GBK编码
# print(sys.getdefaultencoding())

pku_training = open('G:\ChineseCut\PKU_GB\pku_training.txt', 'r')
pku_training_content = pku_training.read()
pku_training.close()
# print(pku_training_content)

# 把pku_training.txt中的分词写入pku_training_words_result.txt

pku_train_word_list = pku_training_content.split()
pku_train_word_set =set()
for eachWord in pku_train_word_list:
    pku_train_word_set.add(eachWord)

# 写入结果
pku_training = open('G:\ChineseCut\PKU_GB\pku_training_result.txt', 'w')
pku_training.close()
pku_training = open('G:\ChineseCut\PKU_GB\pku_training_result.txt', 'w+')
for eachWord in pku_train_word_set:
    pku_training.write(eachWord)
    pku_training.write('\n')
pku_training.close()




