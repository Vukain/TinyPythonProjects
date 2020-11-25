import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = 0.2
korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)
k1 = plt.bar(index, korea_scores, bar_width, alpha=.8, label="Korea", color=(.3, .3, .7))
c1 = plt.bar(index + bar_width, canada_scores, bar_width, alpha=.8, label="Canada", color=(.3, .7, .3))
ch1 = plt.bar(index + 2*bar_width, china_scores, bar_width, alpha=.8, label="China", color=(.7, .3, .3))
f1 = plt.bar(index + 3*bar_width, france_scores, bar_width, alpha=.8, label="France", color=(.7, .7, .7))


def create_labels(*args):
    for arg in args:
        for item in arg:
            height = item.get_height()
            plt.text(item.get_x() + item.get_width() / 2, int(height)*1.05, f"{height}", ha='center', va='bottom')


create_labels(k1, c1, ch1, f1)


plt.ylabel("Mean score in PISA")
plt.xlabel("Subjects")
plt.title("Test scores by country")
plt.xticks(index + .3 / 2, ("Math", "Reading", "Science"))
plt.grid(True)

plt.legend(frameon=True, loc=2, bbox_to_anchor=(1, 1))

plt.show()
