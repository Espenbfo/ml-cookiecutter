import click

from training.training_loop import training_loop


@click.command()
def run_training():
    """This function is meant to be a wrapper for the training_loop """
    training_loop()

if __name__ == "__main__":
    run_training()