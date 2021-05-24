import os ,shutil
original_dataset_dir=(r"C:\Users\vipin\pythonProject\PCBDATA\tobeaugmented\non-defected")
#make new folder
base_dir =(r'C:/Users/vipin/PycharmProjects/pythonProject2/newpcb')
os.mkdir(base_dir)

train_dir=os.path.join(base_dir,"train")
os.mkdir(train_dir)

validation_dir=os.path.join(base_dir,"validation")
os.mkdir(validation_dir)

test_dir=os.path.join(base_dir,"test")
os.mkdir(test_dir)

train_defected_dir=os.path.join(train_dir,"defected")
os.mkdir(train_defected_dir)
train_non_defected_dir=os.path.join(train_dir,"nondefected")
os.mkdir(train_non_defected_dir)

validation_defected_dir=os.path.join(validation_dir,"defected")
os.mkdir(validation_defected_dir)
validation_non_defected_dir=os.path.join(validation_dir,"nondefected")
os.mkdir(validation_non_defected_dir)

test_defected_dir=os.path.join(test_dir,"defected")
os.mkdir(test_defected_dir)
test_non_defected_dir=os.path.join(test_dir,"nondefected")
os.mkdir(test_non_defected_dir)

fnames=['{}.jpg'.format(i) for i in range(1,101)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(train_defected_dir,fname)
    shutil.copyfile(src,dst)



fnames=['{}.jpg'.format(i) for i in range(1,208)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(train_non_defected_dir,fname)
    shutil.copyfile(src,dst)



