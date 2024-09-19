# scripts/hyperparameter_search.py

import optuna
from transformers import Trainer, TrainingArguments
from train import load_model_and_data  # Reuse training logic

def objective(trial):
    # Suggest hyperparameters
    learning_rate = trial.suggest_float('learning_rate', 1e-5, 5e-5)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])
    epochs = trial.suggest_int('epochs', 3, 10)

    # Set training arguments
    training_args = TrainingArguments(
        output_dir="./models/optuna_model/",
        evaluation_strategy="epoch",
        learning_rate=learning_rate,
        per_device_train_batch_size=batch_size,
        num_train_epochs=epochs,
        weight_decay=0.01,
        load_best_model_at_end=True
    )

    # Load model and dataset
    model, dataset = load_model_and_data('imdb', 'bert-base-uncased')
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset['train'],
        eval_dataset=dataset['test'],
    )

    # Train and evaluate
    trainer.train()
    eval_results = trainer.evaluate()

    # Return evaluation metric for trial
    return eval_results['eval_loss']

# Optimize hyperparameters with Optuna
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=10)

# Print best hyperparameters
print("Best hyperparameters:", study.best_params)
