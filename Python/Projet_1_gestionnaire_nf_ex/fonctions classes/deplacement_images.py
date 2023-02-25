def deplacement_images(liste_co_image,liste_image_a_deplacer,coef_add_x,coef_add_y):
    
    for z in range(len(liste_image_a_deplacer)):
        liste_co_image[liste_image_a_deplacer[z]] = (liste_co_image[liste_image_a_deplacer[z]][0]+coef_add_x,liste_co_image[liste_image_a_deplacer[z]][1]+coef_add_y)

    return liste_co_image