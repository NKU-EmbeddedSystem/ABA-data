import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

names = ['blackscholes','bodytrack', 'canneal', 'facesim', 'fluidanimate', 'freqmine', 'swaptions', 'x264']
fig = plt.figure()
fig.subplots_adjust(left=0.05,right=0.95,bottom=0.07,top=0.90, wspace=0.1,hspace=0.15 )
plt.axis('off')
i = 1
width = 0.3
x_labels = ['1', '2', '4', '8', '16', '32', '64']
index = np.arange(len(x_labels))
for name in names:
    num = 240 + i
    i += 1
    fig.add_subplot(num)
    plt.title(name, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    data = pd.read_table(name + '-HST.dat',sep='\t',index_col=0)
    native = data['native']
    exclusive = data['exclusive']
    instrument = data['instrument']
    empty = data['mprotect']
    print(name, native.values)
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='HST', hatch='/', tick_label=x_labels, color='white')
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='PST', hatch='\\', tick_label=x_labels, color='white')
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='Pico-ST', hatch='.', tick_label=x_labels, color='white')
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='native', tick_label=x_labels, color='white')
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='exclusive', tick_label=x_labels, color=(249 / 255, 196 / 255, 153 / 255))
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='instrument', tick_label=x_labels, color=(204 / 255, 194 / 255, 217 / 255))
    plt.bar(index, empty.values, width = 0.33, ec='black', ls='-', label='mprotect', tick_label=x_labels, color=(143 / 255, 200 / 255, 237 / 255))
    if i == 6:
        plt.legend(fontsize=14)

    plt.bar(index, native.values, width = 0.33, ec='black', ls='-', label='native', hatch='/', color='white')
    plt.bar(index, exclusive.values, width = 0.33, ec='black', ls='-', label='exclusive', hatch='/', bottom=native.values, color=(249 / 255, 196 / 255, 153 / 255))
    plt.bar(index, instrument.values, width = 0.33, ec='black', ls='-', label='instrument', hatch='/', bottom=native.values+exclusive.values, tick_label=x_labels, color=(204 / 255, 194 / 255, 217 / 255))
    
    data = pd.read_table(name + '-PST.dat',sep='\t',index_col=0)
    native = data['native']
    exclusive = data['exclusive']
    mprotect = data['mprotect']
    print(name, native.values)
    plt.bar(index + width, mprotect.values, width = 0.33, ec='black', ls='-', label='mprotect', hatch='\\', bottom=native.values+exclusive.values, color=(143 / 255, 200 / 255, 237 / 255))
    
    plt.bar(index + width, native.values, width = 0.33, ec='black', ls='-', label='native', hatch='\\', color='white')
    plt.bar(index + width, exclusive.values, width = 0.33, ec='black', ls='-', label='exclusive', hatch='\\', bottom=native.values, color=(249 / 255, 196 / 255, 153 / 255))

    data = pd.read_table(name + '-Pico.dat',sep='\t',index_col=0)
    native = data['native']
    exclusive = data['exclusive']
    instrument = data['instrument']
    plt.bar(index + width * 2, native.values, width = 0.33, ec='black', ls='-', label='native', hatch='.', color='white')
    plt.bar(index + width * 2, exclusive.values, width = 0.33, ec='black', ls='-', label='exclusive', hatch='.', bottom=native.values, color=(249 / 255, 196 / 255, 153 / 255))
    plt.bar(index + width * 2, instrument.values, width = 0.33, ec='black', ls='-', label='instrument', hatch='.', bottom=native.values+exclusive.values, tick_label=x_labels, color=(204 / 255, 194 / 255, 217 / 255))

    if i > 5:
        plt.xlabel('threads', fontsize=18)
    if i == 2 or i == 6:
        plt.ylabel('elapsed time\s', fontsize=18)
    # fig.set_xlabel('threads')
    # fig.set_ylabel('elapsed time\s')

# font={'family':'serif',
#     'style':'italic',
#     'weight':'normal',
#     'color':'red',
#     'size':22
# }
# plt.text(11000,36000,'OS_longitude:',fontdict=font)
# plt.suptitle('Overhead Analysis of Pico-ST, HST and PST')
plt.show()

