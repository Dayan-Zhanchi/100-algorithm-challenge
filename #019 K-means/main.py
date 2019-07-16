import k_means as km
import elbow_method as em

def main():
    # construct the clusters and plot them
    samples, c = 800, 5
    data = km.generate_random_blobs(samples, c)
    km.plot_blobs(data)
    centers, clusters = km.k_means(data, c)
    km.plot_clusters(centers, clusters, data)

    # validate the choice of k with elbow and plot
    # the choice of
    sum_of_squared_distances = em.elbow_method(data)
    em.plot_elbow(sum_of_squared_distances)

if __name__ == '__main__':
    main()