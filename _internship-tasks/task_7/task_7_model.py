import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


# Load Dataset to DataFrame
X = pd.read_csv('task_7_dataset/Dataset_X.csv')
y = pd.read_csv('task_7_dataset/Dataset_y.csv')
X = X.drop(X.columns[0], axis=1)
y = y.drop(y.columns[0], axis=1)

# Split to Train and Test Datasets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Convert the Validation Data to JSON format
test_X = val_X.head(10)
json_data = test_X.to_json()
# Save it to a file
with open('test_data.json', 'w') as json_file:
    json_file.write(json_data)

# Rebuild the neural network model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=[13]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
# Compile the model
model.compile(
    optimizer='adam',
    loss='mae',
)
# Train the model
history = model.fit(
    train_X, train_y,
    validation_data=(val_X, val_y),
    batch_size=512,
    epochs=50,
)

# Make predictions on the validation set
val_predictions = model.predict(val_X)

# Evaluate the model on the validation set
val_loss = model.evaluate(val_X, val_y)
print(f"Validation Loss (MAE): {val_loss}")

# Save the trained model to disk
model.save('trained_model.h5')