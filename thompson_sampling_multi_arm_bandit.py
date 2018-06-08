import numpy as np
output = False


# generate sample data

N=2000
conversions = {'best':0.06,'medium':0.05,'low':0.03}
result_dict = dict()
for group, conversion in conversions.iteritems():
    for i in range(N):
        if random.random() > conversion:
            out.append(0)
        else:
            out.append(1)
    result_dict[group]=out


    
# thompson sampling   

arms_params = {'best':{'alpha':1,'beta':1},
               'medium':{'alpha':1,'beta':1},
               'low':{'alpha':1,'beta':1}}

arms_probs = {'best': 0, 'medium': 0, 'low':0}

cumulative_success = 0

for i in range(N):
    probs = []
    for arm,prob in arms_probs.iteritems():
        arms_probs[arm] = np.random.beta(
                                arms_params[arm]['alpha'],
                                arms_params[arm]['beta'])

    best_arm_to_pull = max(arms_probs, key=arms_probs.get)

    if result_dict[best_arm_to_pull][i] == 1:
        arms_params[best_arm_to_pull]['alpha'] += 1

    else:
        arms_params[best_arm_to_pull]['beta'] += 1
        
    if output:
        print (result_dict['best'][i],result_dict['medium'][i],result_dict['low'][i],best_arm_to_pull)
        
    cumulative_success += result_dict[best_arm_to_pull][i]
    

print ('total number of iterations: %s' % N)
print ('')
print('Real population ratios :')
print conversions
print ('')
print ('success %s out of %s trials, conversion: %.4f' % (cumulative_success,N,cumulative_success / float(N)))
print ('')
print ('final parameters of the model')
print arms_params