library(dplyr)
library(uuid)
library(purrr)

n_rows <- 100
tibble(
  id = map_chr(1:n_rows, UUIDgenerate),
  description = sample(letters, n_r)
)