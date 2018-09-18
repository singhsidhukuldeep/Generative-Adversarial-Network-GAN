from GAN import GAN

gan = GAN()
gan.train(epochs=300000, batch_size=32, sample_interval=200)
