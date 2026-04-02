import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
   real,fake=np.array(real_scores),np.array(fake_scores)
   wcl=np.mean(fake) - np.mean(real)
   return wcl