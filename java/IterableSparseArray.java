package com.example.testdate;

import java.util.Iterator;

import android.util.SparseArray;

public class IterableSparseArray<T> extends SparseArray<T> {

	private abstract class IndexIterator<E> implements Iterator<E> {
		protected int mIndex = 0;

		@Override
		public boolean hasNext() {
			return mIndex < size();
		}

		@Override
		public void remove() {
			removeAt(mIndex);
		}
	}

	public static class Entry<T> {
		final int key;
		final T value;

		Entry(int key, T value) {
			this.key = key;
			this.value = value;
		}
	}

	public IterableSparseArray() {
		super();
	}

	public IterableSparseArray(int initialCapacity) {
		super(initialCapacity);
	}

	private static <E> Iterable<E> createIterable(final Iterator<E> iter) {
		return new Iterable<E>() {
			@Override
			public Iterator<E> iterator() {
				return iter;
			}
		};
	}

	public Iterable<T> values() {
		return createIterable(new IndexIterator<T>() {
			@Override
			public T next() {
				return valueAt(mIndex++);
			}
		});
	}

	public Iterable<Integer> keys() {
		return createIterable(new IndexIterator<Integer>() {
			@Override
			public Integer next() {
				return keyAt(mIndex++);
			}
		});
	}

	public Iterable<Entry<T>> entries() {
		return createIterable(new IndexIterator<Entry<T>>() {
			@Override
			public Entry<T> next() {
				Entry<T> e = new Entry<T>(keyAt(mIndex), valueAt(mIndex));
				mIndex++;
				return e;
			}
		});
	}
}