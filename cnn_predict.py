from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np


def predict(path):
    # Load the trained model
    loaded_model = load_model("derma.h5")  # Use the path where you saved your trained model

    # Function to preprocess the image for prediction
    def preprocess_image(image_path):
        img = image.load_img(image_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize the image
        return img_array

    # Example usage:
    # image_path = "image_42_jpg.rf.5fef579fe8c25861c1e45155f13dfbd9.jpg"  # Replace with the path to your new image
    processed_image = preprocess_image(path)

    # Make predictions
    predictions = loaded_model.predict(processed_image)

    # Map predicted class index to label
    class_labels = ['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions','Atopic Dermatitis Photos',
                    'Bullous Disease Photos','Cellulitis Impetigo and other Bacterial Infections','Eczema Photos','Exanthems and Drug Eruptions',
                    'Hair Loss Photos Alopecia and other Hair Diseases','Herpes HPV and other STDs Photos','Invalid Image','Light Diseases and Disorders of Pigmentation',
                    'Lupus and other Connective Tissue diseases','Melanoma Skin Cancer Nevi and Moles','Nail Fungus and other Nail Disease','Normal Skin',
                    'Poison Ivy Photos and other Contact Dermatitis','Psoriasis pictures Lichen Dermatosis and related diseases','Scabies Lyme Disease and other Infestations and Bites',
                    'Seborrheic Keratoses and other Benign Tumors','Systemic Disease','Tinea Ringworm Candidiasis and other Fungal Infections',
                    'Urticaria Hives','Vascular Tumors','Vasculitis Photos','Viral infections','Warts Molluscum']
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]

    print("Predicted Class:", predicted_class_label)
    
    return predicted_class_label
