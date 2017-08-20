 ## Plot and save
   plt.figure()
   plt.title("%d data points" % (values))
   plt.hist(parameter_values,50, normed=True, alpha=0.9)
   plt.axvline(x=lower_90,linewidth=2,linestyle='dashed',color='k')
   plt.axvline(x=mean_val,linewidth=2, color='k')
   plt.axvline(x=upper_90,linewidth=2,linestyle='dashed',color='k')
   plt.xlabel("%s" % parameter)
   plt.grid()
   # Removed the priors, add them if you fancy
   ## Plot priors for derived spin parameters
   #if parameter=="chi_p":
      #prior=np.loadtxt("priors/chi_p_prior.txt")
      #plt.hist(prior,50,normed=True,alpha=0.6)
   #elif parameter=="chi_eff":
      #prior=np.loadtxt("priors/chi_eff_prior.txt")
      #plt.hist(prior,50,normed=True,alpha=0.6)
   plt.savefig("%s.png" % savename)
   print "Plot saved as %s.png" % savename
