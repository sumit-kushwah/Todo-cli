from utils import fm, prompter, colors
from commands import listit

tasks = fm.get()

def byText(exp):
    results = []
    for task in tasks:
        if task.isTextFound(exp):
            results.append(task)
    return results

def byLabel(label):
    results = []
    for task in tasks:
        if label in task.labels:
            results.append(task)
    return results

def find(args):
    text = args.text
    ftasks = []
    if text[0] == '#':
        label = text[1:]
        ftasks = byLabel(label)
        title = str(len(ftasks)) + ' ' + f" task found with label '{label}'"
    else:
        ftasks = byText(text)
        title = str(len(ftasks)) + ' ' + f" task found with re '{text}'"

    dids = listit.todayIds(ftasks)
    ids = prompter.prompt(ftasks, title, dids, args.verbose, args.sort)
    listit.toToday(ids)
    prompter.scheduleMsg(len(ids))
    

    


    