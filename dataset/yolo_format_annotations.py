import os
import xml.etree.ElementTree as ET


def main():
   path="./annotations/"
   for filename in os.listdir(path):
     tree = ET.parse(path + filename)
     root = tree.getroot()
     for size in root.findall('size'):
       picture_width = int(size.find('width').text)
       picture_heigth = int(size.find('height').text)
     labels = []
     xMins = []
     xMaxs = []
     yMins = []
     yMaxs = []
     dw = 1./picture_width
     dh = 1./picture_heigth
     i = 0
     txtName = filename.replace('.xml', '.txt')
     outF = open('./images/' + txtName, "w")
     for object_ in root.findall('object'):
       tmpLabel = object_.find('name').text
       if tmpLabel == 'without_mask':
         tmpLabel = '0'
       elif tmpLabel == 'mask_weared_incorrect':
         tmpLabel = '1'
       else:
         tmpLabel = '2'
       labels.append(tmpLabel)
       box = object_.find('bndbox')
       xMins.append(int(box.find('xmin').text))
       yMins.append(int(box.find('ymin').text))
       xMaxs.append(int(box.find('xmax').text))
       yMaxs.append(int(box.find('ymax').text))
       
       x = (xMaxs[i] + xMins[i])/2.0
       y = (yMaxs[i] + yMins[i])/2.0
       width = xMaxs[i] - xMins[i]
       height = yMaxs[i] - yMins[i]
       x = x*dw
       y = y*dh
       width = width*dw
       height = height*dh

       line = labels[i] + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' '  + str(height)
       outF.write(line)
       outF.write('\n')
       i += 1
     outF.close()


if __name__ == '__main__':
   main()