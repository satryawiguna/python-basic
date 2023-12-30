try:
    file = open('simple.txt','r')
    file.write('Wite to simple text')
# except IOError:
except:
    print('ERROR: Could not find file or read data!')
# else:
#     print('SUCCESS')
#     file.close()
finally:
    print('I always work no matter what')