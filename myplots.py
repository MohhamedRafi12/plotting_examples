import numpy as np
import matplotlib.pyplot as plt 

def plot_random_gauss():
  plt.figure(figsize=(10,10))

  norms = np.random.normal(loc=100, scale=6.04, size=10000)
  plt.ylabel('frequency')
  plt.xlabel('x')
  plt.title('random gauss')
  plt.hist(norms, bins=np.linspace(50, 150, 100))

  plt.savefig('./canvas1_py.png')


def plot_err_hist(ax, bins, set, label):
  counts, _ = np.histogram(set, bins=bins)
  bin_centers = (bins[1:] + bins[:-1])/2
  ax.errorbar(bin_centers, counts, yerr=np.sqrt(counts), label=label, ls='dotted')


def plot_random_gauss_2x2():
  fig, axs= plt.subplots(2, 2, figsize=(15,15))

  axs = axs.flatten()
  norms = np.random.normal(loc=100, scale=6.04, size=10000)

  g2 = np.random.normal(100, 10, 10000//2)
  
  offsets = [
    norms,
    np.concatenate([norms, np.random.uniform(50, 150, size=10000//3)]),
    np.concatenate([norms, (np.random.pareto(a=1, size=10000*30) + 1) * 10 + 40]),
    np.concatenate([norms, g2])
  ]

  titles = [
    'Random Gauss',
    'Gauss + Offset',
    'Gauss + Offset2',
    'Double Gauss'
  ]

  for i,ax in enumerate(axs):
    ax.set_title(titles[i])
    plot_err_hist(ax, np.linspace(50, 150, 100), offsets[i], label='')
    if i == 2:
      ax.set_yscale('log')

    # ROOT-style stats
    entries = len(offsets[i])
    mean = offsets[i].mean()
    std = offsets[i].std()

    textstr = '\n'.join((
        f'Entries = {entries}',
        f'Mean    = {mean:.2f}',
        f'Std Dev = {std:.2f}'
    ))

    ax.text(0.98, 0.95, textstr,
            transform=ax.transAxes,
            fontsize=10,
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='white', alpha=0.7))


    ax.set_xlabel('x')
    ax.set_ylabel('frequency')

  plt.savefig('./canvas2_py.png')
  plt.tight_layout()

if __name__ == "__main__":
  plot_random_gauss()
  plot_random_gauss_2x2()