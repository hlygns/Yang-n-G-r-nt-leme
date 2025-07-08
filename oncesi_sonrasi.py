import leafmap.foliumap as lm
img1=r'C:\Users\HP\Desktop\KC_House\WhatsApp Image 2025-07-08 at 11.16.01 (1).jpeg'
img2=r'C:\Users\HP\Desktop\KC_House\WhatsApp Image 2025-07-08 at 11.16.01.jpeg'
lm.image_comparison(img1,img2,
label1='Önce',
label2='Sonra',
starting_position=50,
out_html='orman_once_sonra.html')