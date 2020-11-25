import os
import xml.etree.ElementTree as ET
# Function to rename multiple files
def main():
   i = 0
   path="./annotations/"
   for filename in os.listdir(path):
     tree = ET.parse(path + filename)
     root = tree.getroot()
     for f in root.find('filename'):
       print('filename',f.text)
     for size in root.findall('size'):
       picture_width = int(size.find('width').text)
       picture_heigth = int(size.find('height').text)
       print('picture_width', picture_width)
       print('picture_heigth', picture_heigth)
     labels = []
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
       xmin = int(box.find('xmin').text)
       ymin = int(box.find('ymin').text)
       xmax = int(box.find('xmax').text)
       ymax = int(box.find('ymax').text)
       print('xmin',xmin)
       print('ymin',ymin)
       print('xmax',xmax)
       print('ymax',ymax)
      
     dw = 1./picture_width
     dh = 1./picture_heigth
     x = (xmax + xmin)/2.0
     y = (ymax + ymin)/2.0
     width = xmax - xmin
     height = ymax - ymin
     x = x*dw
     y = y*dh
     width = width*dw
     height = height*dh


     txtName = filename.replace('.xml', '.txt')
     print(txtName)
     #line = label + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' '  + str(height)
     #outF = open('./images/' + txtName, "w")
      # write line to output file
     #outF.write(line)
     #outF.close()
     break

### support multiple objects detection!!!

# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()