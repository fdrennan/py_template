library(purrr)

make_df <- function() {
  data.frame(
    id = c('a', 'a', 'b', 'c'),
    description = c('one', 'two', 'three', 'four'),
    timestamp = c(1, 2, 3, 4)
  )
}

walk(
  1:4,
  function(x) {
    write.csv(make_df(), paste0(x, '.csv'))
  }
)

