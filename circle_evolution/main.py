"""CLI for Circle Evolution"""

import argparse

import numpy as np

from circle_evolution.evolution import Evolution

import circle_evolution.helpers as helpers


SIZE_OPTIONS = {1: (64, 64), 2: (128, 128), 3: (256, 256), 'auto': None}


def main():
    """Entrypoint of application"""
    parser = argparse.ArgumentParser(description="Circle Evolution CLI")

    parser.add_argument("image", type=str, help="Image to be processed")
    parser.add_argument("--size", choices=SIZE_OPTIONS.keys(), default='auto', help="Dimension of the image")
    parser.add_argument("--genes", default=256, type=int, help="Number of genes")
    parser.add_argument("--max-generations", type=int, default=500000)
    args = parser.parse_args()

    target = helpers.load_target_image(args.image, size=SIZE_OPTIONS[args.size])

    output_img_dimensions = SIZE_OPTIONS[args.size] or target.shape
    evolution = Evolution(output_img_dimensions, target, genes=args.genes)
    evolution.evolve(max_generation=args.max_generations)

    evolution.specie.render()

    helpers.show_image(evolution.specie.phenotype)

    output_path_checkpoint = "checkpoint-{}.txt".format(evolution.generation)
    np.savetxt(output_path_checkpoint, evolution.specie.genotype)


if __name__ == "__main__":
    main()
