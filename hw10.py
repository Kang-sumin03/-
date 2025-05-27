import os

filename='score.bin'

def input_scores() :
    score =[]
    i=1
    while True:
        n=int(input(f'#{i}? '))
        if n>=0 :
            score.append(n)
        
        else :
            break
        i=i+1
    return score

def get_average(score) :
    total = 0
    for n in score:
        total += n

    print(f'평균:{total/len(score):.1f}')
    
def show_scores(score) :
    for n in score:
        print(n, end=' ')
    print()


def save_data(score,filepath) :
    with open(filepath, 'w', encoding='utf8') as file :
        for n in score :
            file.write(f'{n}\n')
def load_data(filepath):
    lines=[]
    with open(filepath, 'r', encoding='utf8') as file :
        for line in file :
            lines.append(int(line.strip('\n')))
    return lines

if os.path.exists(filename):
    print('[파일 읽기]')
    score_list=load_data(filename)
    show_scores(score_list)
    get_average(score_list)
else:
    score_list=[]

while True:
    print('[점수 입력]')
    new_scores=input_scores()
    if not new_scores:
        break
    score_list.extend(new_scores)
    print()

    print('[점수 출력]')
    print('개인점수 :', end='')
    show_scores(score_list,)
    get_average(score_list)
    
    save_data(score_list, filename)
