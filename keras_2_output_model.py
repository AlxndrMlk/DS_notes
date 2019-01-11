from keras.layers import Input, Dense
from keras.models import Model

# Define the input
input_tensor = Input(shape=(2,))

# Define the output
output_tensor = Dense(2)(input_tensor)

# Create a model
model = Model(input_tensor, output_tensor)

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')

# Fit the model
model.fit(games_tourney_train[['seed_diff', 'pred']],
  		  games_tourney_train[['score_1', 'score_2']],
  		  verbose=True,
  		  epochs=500,
  		  batch_size=16384)

# Print the model's weights
print(model.get_weights())

# Print the column means of the training data
print(games_tourney_train.mean())
