import os
import re
import pandas as pd
import matplotlib.pyplot as plt


def rename_size(size):
    if size <= 512:
        return str(size) + 'K'
    elif size <= 512 * 1024:
        return str(size // 1024) + 'M'
    elif size <= 512 * 1024 * 1024:
        return str(size // (1024 * 1024)) + 'G'

def get_speed(dir_name, columns):
    data = []
    for (dirpath, dirnames, filenames) in os.walk(dir_name):
        for filename in filenames:
            if ".txt" in filename:
                with open(dir_name + "/" + filename) as f:
                    lines = f.readlines()
                    for line in lines:
                        pattern_digit = re.compile("[0-9\s]+")
                        pattern_space = re.compile("[\s]+")
                        if pattern_digit.fullmatch(line) and not pattern_space.fullmatch(line):
                            data.append([int(s) for s in line.split()])
            

    df = pd.DataFrame(data, columns=columns)
    df = df.groupby('size').agg("mean").reset_index()
    return df
    #df = df.round()

columns = ['size', 'reclen', 'write', 'rewrite', 'read', 'reread', 'random_read', 'random_write', 'bkwd_read', 'record_rewrite', 'stride_read', 'fwrite', 'frewrite', 'fread', 'freread']

df_NTFS = get_speed('NTFS', columns = columns)
df_ext4 = get_speed('ext4', columns = columns)


plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['read'], label = 'NTFS')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['read'], label = 'ext4')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('read.pdf')




plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['write'], label = 'NTFS write', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['rewrite'], '--', label = 'NTFS rewrite', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['write'], label = 'ext4 write', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['rewrite'], '--', label = 'ext4 rewrite', color='tab:orange')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('write.pdf')


'''
plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')



plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('write_NTFS.pdf')
'''



plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['read'], label = 'NTFS read', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['random_read'], '--', label = 'NTFS random read', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['read'], label = 'ext4 read', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['random_read'], '--', label = 'ext4 random read', color='tab:orange')

plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
plt.savefig('random_read.pdf')




plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['write'], label = 'NTFS write', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['random_write'], '--', label = 'NTFS random write', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['write'], label = 'ext4 write', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['random_write'], '--', label = 'ext4 random write', color='tab:orange')

plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
plt.savefig('random_write.pdf')




'''
plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')



plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('random_read_NTFS.pdf')
'''


'''
plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')


plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('random_write_NTFS.pdf')
'''




df_NTFS_mmap = get_speed('NTFS_mmap', columns = columns[:-4])
df_ext4_mmap = get_speed('ext4_mmap', columns = columns[:-4])


plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['write'], label = 'NTFS write', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS_mmap['size']], df_NTFS_mmap['write'], '--', label = 'NTFS write w/ mmap()', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['write'], label = 'ext4 write', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4_mmap['size']], df_ext4_mmap['write'], '--', label = 'ext4 write w/ mmap()', color='tab:orange')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('write_mmap.pdf')



plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS['size']], df_NTFS['read'], label = 'NTFS read', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS_mmap['size']], df_NTFS_mmap['read'], '--', label = 'NTFS read w/ mmap()', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4['size']], df_ext4['read'], label = 'ext4 read', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4_mmap['size']], df_ext4_mmap['read'], '--', label = 'ext4 read w/ mmap()', color='tab:orange')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('read_mmap.pdf')


'''
plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')



plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('write_mmap_ext4.pdf')
'''

df_NTFS_small = get_speed('NTFS_small', columns = columns)
df_ext4_small = get_speed('ext4_small', columns = columns)
df_NTFS_small_mmap = get_speed('NTFS_small_mmap', columns = columns[:-4])
df_ext4_small_mmap = get_speed('ext4_small_mmap', columns = columns[:-4])

plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(13, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS_small['size']], df_NTFS_small['write'], label = 'NTFS write', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS_small_mmap['size']], df_NTFS_small_mmap['write'], '--', label = 'NTFS write w/ mmap()', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4_small['size']], df_ext4_small['write'], label = 'ext4 write', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4_small_mmap['size']], df_ext4_small_mmap['write'], '--', label = 'ext4 write w/ mmap()', color='tab:orange')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('write_small_mmap.pdf')





plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(6.5, 5))

ax.set_xlabel('File Size')
ax.set_ylabel('Speed (KBytes/s)')

plt.plot([rename_size(i) for i in df_NTFS_small['size']], df_NTFS_small['read'], label = 'NTFS read', color='tab:blue')
plt.plot([rename_size(i) for i in df_NTFS_small_mmap['size']], df_NTFS_small_mmap['read'], '--', label = 'NTFS read w/ mmap()', color='tab:blue')
plt.plot([rename_size(i) for i in df_ext4_small['size']], df_ext4_small['read'], label = 'ext4 read', color='tab:orange')
plt.plot([rename_size(i) for i in df_ext4_small_mmap['size']], df_ext4_small_mmap['read'], '--', label = 'ext4 read w/ mmap()', color='tab:orange')

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('read_small_mmap.pdf')