import React from 'react'

const Modal = ({ isOpen, onClose, title, data }) => {
  if (!isOpen) return null
  return (
    <div className='fixed inset-0 flex justify-center items-center bg-gray-900 bg-opacity-50'>
      <div className='bg-white p-6 rounded-lg shadow-xl'>
        <h2 className='text-3xl font-bold mb-4'>{title}</h2>
        <p className='text-xl'>{data}</p>
        <button onClick={onClose} className='mt-4 px-6 py-2 bg-black text-white rounded-md'>
          Close
        </button>
      </div>
    </div>
  )
}

export default Modal
