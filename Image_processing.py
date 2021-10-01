from PIL import Image,ImageFilter

ch=0
while(1):
    print('\t~~~Welcome to the image processing~~\n\n/The list of the operation is given below ===> \n\n\n')
    print("0. Exit\n1.Transpose\n2.Rotate\n3.Make a new file with background colour\n4.Transparent Image file\n5.Apply Filter on Image\n0.Exit\n\n\n")
    ch=int(input("Enter your choice for operation: "))
    if (ch==1):
        name=input('Enter the name of image: ')
        save=input('Enter the name to save: ')
        image = Image.open(name)
        image.show()
        transposed_img=image.transpose(Image.FLIP_LEFT_RIGHT)
        transposed_img.save(save)
        transposed_img.show()
    elif(ch==2):
        name=input('Enter the name of image: ')
        save=input('Enter the name to save: ')
        angle=float(input('Enter the angle to be rotate'))
        image = Image.open(name)
        image.show()
        rotate_img=image.rotate(angle)
        rotate_img.save(save)
        rotate_img.show()
    elif(ch==3):
        name=input('Enter the Colour name for Background Colour of Image: ')
        save=input('Enter the name to save the file: ')
        im=Image.new('RGBA',(100,200),name)
        im.show()
        im.save(save)
    elif(ch==4):
        save=input('Enter the name to save the file: ')
        im2=Image.new('RGBA',(20,20))
        im2.show()
        im2.save(save)
    elif (ch==5):
        choice=0
        while(1):
            print('Choose your choice to apply the Filter: ')
            print('1.Black and white\n2.Blur image\n3.Emboss\n4.Contour\n5.Edge enhance\n6.More enhance7.Sharpen\n8.Detailed\n0.Exit')
            choice=int(input("Enter your choice for operation: "))
            if(choice == 1):         
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')      
                greyscale_image = image.convert('L')
                greyscale_image.show()
                greyscale_image.save(save)
            elif(choice==2):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                bs=int(input('Enter the number to do the Blur Scale: '))
                im=image.filter(ImageFilter.BoxBlur(bs))
                im.show()
                im.save(save)
            elif(choice==3):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.EMBOSS)
                im.show()
                im.save(save)
            elif(choice==4):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.CONTOUR)
                im.show()
                im.save(save)
            elif(choice==5):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.EDGE_ENHANCE)
                im.show()
                im.save(save)
            elif(choice==6):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                im.show()
                im.save(save)
            elif(choice==7):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.SHARPEN)
                im.show()
                im.save(save)
            elif(choice==8):
                name=input('Enter the name of image: ')
                image = Image.open(name)
                save=input('Enter the name to save: ')
                im=image.filter(ImageFilter.DETAIL)
                im.show()
                im.save(save)
            elif(choice==0):
                break;
            else:
                print('Invalid Choice')
    elif(ch==0):
        print('Exiting program!')
        break;
    else:
        print('Invalid Choice')
