package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var counter = int64(0)
	var wg sync.WaitGroup

	
	for id := 0; id < 16; id++ {
		my_id := id
		wg.Add(1)
		go func () {
			defer wg.Done()
			var success = false
			var updatedCounter int64
			var readCounter int64
			for !success {
				readCounter = counter
				updatedCounter = readCounter + 1
				success = atomic.CompareAndSwapInt64(&counter, readCounter, updatedCounter)
			}
			fmt.Println(my_id)
		}()
	}

	wg.Wait()
}