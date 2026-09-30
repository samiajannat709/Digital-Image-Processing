import cv2
import matplotlib.pyplot as plt


image = cv2.imread('images.png')


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()


print("Image dimensions:", image.shape)


print("Pixel value at (100,100):", image[100, 100])


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


print("Grayscale dimensions:", gray.shape)


plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


resized = cv2.resize(image, (300, 300))

plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')
plt.axis('off')
plt.show()

cropped = image[100:300, 100:300]

plt.imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.axis('off')
plt.show()


cv2.imwrite('gray_output.jpg', gray)

print("Grayscale image saved successfully!")