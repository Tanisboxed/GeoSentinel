import numpy as np 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Adam 
from sklearn.model_selection import train_test_split 
from data_preprocessor import DataPreprocessor, load_and_merge_data

class ConflictClassifier:
    def __init__(self, input_dim):
        self.model = Sequential([
            Dense(64, activation ='relu', input_dim=input_dim),
            Dropout(0.2),
            Dense(32, activation = 'relu'),
            Dropout(0.2),
            Dense(16, activation='relu'),
            Dense(3, activation='softmax')
        ])

        self.model.compile(optimizer= Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])

    def train(self, X_train, y_train, epochs=50, batch_size=32, validation_split=0.2):
        return self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=validation_split,verbose=1)

    def predict(self, X):
        return self.model.predict(X)
    
    def save(self, filepath):
        self.model.save(filepath)
    
    @classmethod
    def load(cls, filepath):
        loaded_model = tf.keras.models.load_model(filepath)
        instance = cls(loaded_model.input_shape[1])
        instance.model = loaded_model 
        return instance

def prepare_target(data):
    event_type_map = {
        'Battle-No change of territory': 0,
        'Armed clash': 0,
        'Attack': 0,
        'Air/drone strike': 1,
        'Artillery/missile attack': 1,
        'Protest': 2,
        'Riot': 2,
        'Peaceful protest': 2
    }
    y = data['event_type'].map(event_type_map)
    return tf.keras.utils.to_categorical(y, num_classes=3)

if __name__ == "__main__":
    data = load_and_merge_data()
    preprocessor = DataPreprocessor()
    X = data[['latitude', 'longitude', 'cloud_cover', 'event_type', 'actor1', 'actor2', 'location', 'notes']]
    X_processed = preprocessor.fit_transform(X)
    y = prepare_target(data)

    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
    classifier = ConflictClassifier(input_dim=X_processed.shape[1])
    history = classifier.train(X_train, y_train)

    loss, accuracy = classifier.model.evaluate(X_test, y_test)
    print(f"Test accuracy: {accuracy:.2f})

    classifier.save('models/conflict_classifier.h5')
    print("Model Trained ")