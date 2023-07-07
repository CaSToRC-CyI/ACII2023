#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import read_acq_file, rescale

#%%

# Dataset 2 - Low Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/LowAlexithymics/'
#%%
participant_112301 = {'112301': {'acq_data': read_acq_file(folder_path, '112301.acq'),\
                                 'group_label': info_dict[112301][0],\
                                 'dataset': info_dict[112301][1]}}
    
participant_112352 = {'112352': {'acq_data': read_acq_file(folder_path, '112352.acq'),\
                                 'group_label': info_dict[112352][0],\
                                 'dataset': info_dict[112352][1]}}

participant_112358 = {'112358': {'acq_data': read_acq_file(folder_path, '112358.acq'),\
                                 'group_label': info_dict[112358][0],\
                                 'dataset': info_dict[112358][1]}}

participant_112359 = {'112359': {'acq_data': read_acq_file(folder_path, '112359.acq'),\
                                 'group_label': info_dict[112359][0],\
                                 'dataset': info_dict[112359][1]}}

participant_112364 = {'112364': {'acq_data': read_acq_file(folder_path, '112364.acq'),\
                                 'group_label': info_dict[112364][0],\
                                 'dataset': info_dict[112364][1]}}
    
participant_112365 = {'112365': {'acq_data': read_acq_file(folder_path, '112365.acq'),\
                                 'group_label': info_dict[112365][0],\
                                 'dataset': info_dict[112365][1]}}

participant_122306 = {'122306': {'acq_data': read_acq_file(folder_path, '122306.acq'),\
                                 'group_label': info_dict[122306][0],\
                                 'dataset': info_dict[122306][1]}}

participant_122312 = {'122312': {'acq_data': read_acq_file(folder_path, '122312.acq'),\
                                 'group_label': info_dict[122312][0],\
                                 'dataset': info_dict[122312][1]}}
    
participant_122318 = {'122318': {'acq_data': read_acq_file(folder_path, '122318.acq'),\
                                 'group_label': info_dict[122318][0],\
                                 'dataset': info_dict[122318][1]}}

participant_122319 = {'122319': {'acq_data': read_acq_file(folder_path, '122319.acq'),\
                                 'group_label': info_dict[122319][0],\
                                 'dataset': info_dict[122319][1]}}

participant_122330 = {'122330': {'acq_data': read_acq_file(folder_path, '122330.acq'),\
                                 'group_label': info_dict[122330][0],\
                                 'dataset': info_dict[122330][1]}}

participant_122335 = {'122335': {'acq_data': read_acq_file(folder_path, '122335.acq'),\
                                 'group_label': info_dict[122335][0],\
                                 'dataset': info_dict[122335][1]}}
    
participant_122336 = {'122336': {'acq_data': read_acq_file(folder_path, '122336.acq'),\
                                 'group_label': info_dict[122336][0],\
                                 'dataset': info_dict[122336][1]}}

participant_122342 = {'122342': {'acq_data': read_acq_file(folder_path, '122342.acq'),\
                                 'group_label': info_dict[122342][0],\
                                 'dataset': info_dict[122342][1]}}
    
participant_122347 = {'122347': {'acq_data': read_acq_file(folder_path, '122347.acq'),\
                                 'group_label': info_dict[122347][0],\
                                 'dataset': info_dict[122347][1]}}
    
participant_122348 = {'122348': {'acq_data': read_acq_file(folder_path, '122348.acq'),\
                                 'group_label': info_dict[122348][0],\
                                 'dataset': info_dict[122348][1]}}

participant_211351 = {'211351': {'acq_data': read_acq_file(folder_path, '211351.acq'),\
                                 'group_label': info_dict[211351][0],\
                                 'dataset': info_dict[211351][1]}}

participant_212357 = {'212357': {'acq_data': read_acq_file(folder_path, '212357.acq'),\
                                 'group_label': info_dict[212357][0],\
                                 'dataset': info_dict[212357][1]}}

participant_212363 = {'212363': {'acq_data': read_acq_file(folder_path, '212363.acq'),\
                                 'group_label': info_dict[212363][0],\
                                 'dataset': info_dict[212363][1]}}
    
participant_212366 = {'212366': {'acq_data': read_acq_file(folder_path, '212366.acq'),\
                                 'group_label': info_dict[212366][0],\
                                 'dataset': info_dict[212366][1]}}

participant_222302 = {'222302': {'acq_data': read_acq_file(folder_path, '222302.acq'),\
                                 'group_label': info_dict[222302][0],\
                                 'dataset': info_dict[222302][1]}}

participant_222305 = {'222305': {'acq_data': read_acq_file(folder_path, '222305.acq'),\
                                 'group_label': info_dict[222305][0],\
                                 'dataset': info_dict[222305][1]}}
    
participant_222308 = {'222308': {'acq_data': read_acq_file(folder_path, '222308.acq'),\
                                 'group_label': info_dict[222308][0],\
                                 'dataset': info_dict[222308][1]}}

participant_222317 = {'222317': {'acq_data': read_acq_file(folder_path, '222317.acq'),\
                                 'group_label': info_dict[222317][0],\
                                 'dataset': info_dict[222317][1]}}

participant_222329 = {'222329': {'acq_data': read_acq_file(folder_path, '222329.acq'),\
                                 'group_label': info_dict[222329][0],\
                                 'dataset': info_dict[222329][1]}}

participant_222343 = {'222343': {'acq_data': read_acq_file(folder_path, '222343.acq'),\
                                 'group_label': info_dict[222343][0],\
                                 'dataset': info_dict[222343][1]}}
    
participant_222346 = {'222346': {'acq_data': read_acq_file(folder_path, '222346.acq'),\
                                 'group_label': info_dict[222346][0],\
                                 'dataset': info_dict[222346][1]}}

participant_312361 = {'312361': {'acq_data': read_acq_file(folder_path, '312361.acq'),\
                                 'group_label': info_dict[312361][0],\
                                 'dataset': info_dict[312361][1]}}

participant_312362 = {'312362': {'acq_data': read_acq_file(folder_path, '312362.acq'),\
                                 'group_label': info_dict[312362][0],\
                                 'dataset': info_dict[312362][1]}}
    
participant_312368 = {'312368': {'acq_data': read_acq_file(folder_path, '312368.acq'),\
                                 'group_label': info_dict[312368][0],\
                                 'dataset': info_dict[312368][1]}}

participant_321309 = {'321309': {'acq_data': read_acq_file(folder_path, '321309.acq'),\
                                 'group_label': info_dict[321309][0],\
                                 'dataset': info_dict[321309][1]}}

participant_321316 = {'321316': {'acq_data': read_acq_file(folder_path, '321316.acq'),\
                                 'group_label': info_dict[321316][0],\
                                 'dataset': info_dict[321316][1]}}

participant_321333 = {'321333': {'acq_data': read_acq_file(folder_path, '321333.acq'),\
                                 'group_label': info_dict[321333][0],\
                                 'dataset': info_dict[321333][1]}}
    
participant_322303 = {'322303': {'acq_data': read_acq_file(folder_path, '322303.acq'),\
                                 'group_label': info_dict[322303][0],\
                                 'dataset': info_dict[322303][1]}}

participant_322310 = {'322310': {'acq_data': read_acq_file(folder_path, '322310.acq'),\
                                 'group_label': info_dict[322310][0],\
                                 'dataset': info_dict[322310][1]}}

participant_322315 = {'322315': {'acq_data': read_acq_file(folder_path, '322315.acq'),\
                                 'group_label': info_dict[322315][0],\
                                 'dataset': info_dict[322315][1]}}
    
participant_322322 = {'322322': {'acq_data': read_acq_file(folder_path, '322322.acq'),\
                                 'group_label': info_dict[322322][0],\
                                 'dataset': info_dict[322322][1]}}

participant_322327 = {'322327': {'acq_data': read_acq_file(folder_path, '322327.acq'),\
                                 'group_label': info_dict[322327][0],\
                                 'dataset': info_dict[322327][1]}}

participant_322328 = {'322328': {'acq_data': read_acq_file(folder_path, '322328.acq'),\
                                 'group_label': info_dict[322328][0],\
                                 'dataset': info_dict[322328][1]}}

participant_322334 = {'322334': {'acq_data': read_acq_file(folder_path, '322334.acq'),\
                                 'group_label': info_dict[322334][0],\
                                 'dataset': info_dict[322334][1]}}
    
participant_322338 = {'322338': {'acq_data': read_acq_file(folder_path, '322338.acq'),\
                                 'group_label': info_dict[322338][0],\
                                 'dataset': info_dict[322338][1]}}

participant_322344 = {'322344': {'acq_data': read_acq_file(folder_path, '322344.acq'),\
                                 'group_label': info_dict[322344][0],\
                                 'dataset': info_dict[322344][1]}}

participant_322345 = {'322345': {'acq_data': read_acq_file(folder_path, '322345.acq'),\
                                 'group_label': info_dict[322345][0],\
                                 'dataset': info_dict[322345][1]}}
    
participant_322350 = {'322350': {'acq_data': read_acq_file(folder_path, '322350.acq'),\
                                 'group_label': info_dict[322350][0],\
                                 'dataset': info_dict[322350][1]}}    
