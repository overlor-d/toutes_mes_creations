from PIL import Image



def image_transparence(image,co_souris,co_image,taille_ecran):
    co_image = [co_image[0],co_image[1]]
    cosour = int((co_souris[0]-co_image[0])),int((co_souris[1]-co_image[1]))
    
    image = Image.open(image)
    
    dim_img = int((image.size[0]/1920)*taille_ecran[0]),int((image.size[1]/1080)*taille_ecran[1])
    image = image.resize((dim_img))
    couleurs=image.getpixel((cosour))
    
    if couleurs[3] == 0:
        return False
    else :
        return True